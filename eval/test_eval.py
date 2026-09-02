import json
import time
from pathlib import Path
from app.services.chatbot_service import chat

DATASET_PATH = Path(__file__).parent / "eval_dataset.json"


def run_50_case_eval():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    print("=" * 85)
    print(f"RUNNING 50-CASE BENCHMARK (Local Qwen 1.7B via Ollama)")
    print("=" * 85)

    passed_count = 0
    results = []

    for item in dataset:
        case_id = item["id"]
        category = item["category"]
        session_id = item["user_session"]
        prompt = item["prompt"]

        start_time = time.time()
        try:
            output = chat(session_id, prompt)
        except Exception as e:
            output = f"ERROR: {str(e)}"
        latency = int((time.time() - start_time) * 1000)

        # Multi-dimensional scoring
        passed = True
        failure_reasons = []

        # 1. Keyword assertion (Factuality / Helpfulness)
        if "required_keywords" in item:
            found_any = any(
                kw.lower() in output.lower() for kw in item["required_keywords"]
            )
            if not found_any:
                passed = False
                failure_reasons.append("Missing required factual keywords")

        # 2. Negative assertion (Security / Prompt Leak / Hallucination)
        if "forbidden_keywords" in item:
            found_forbidden = any(
                kw.lower() in output.lower()
                for kw in item["forbidden_keywords"]
            )
            if found_forbidden:
                passed = False
                failure_reasons.append("Leaked forbidden instructions/payload")

        if passed:
            passed_count += 1
            print(f"[PASS] {case_id} | {category} ({latency} ms)")
        else:
            print(
                f"[FAIL] {case_id} | {category} ({latency} ms) -> Reason: {', '.join(failure_reasons)}"
            )
            print(f"       Prompt: {prompt}")
            print(f"       Output: {output[:90]}...")

        results.append(
            {
                "id": case_id,
                "category": category,
                "latency_ms": latency,
                "passed": passed,
            }
        )

    score = (passed_count / len(dataset)) * 100
    print("=" * 85)
    print(
        f"TOTAL EVALUATION SCORE: {passed_count}/{len(dataset)} Passed ({score:.1f}%)"
    )
    print("=" * 85)


if __name__ == "__main__":
    run_50_case_eval()
