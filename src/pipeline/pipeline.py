import pandas as pd
from tqdm import tqdm

def run_classification(transcript_df, classification_chain):
    results = []

    for i,row in tqdm(transcript_df.iterrows(), total=len(transcript_df), desc="Classification of the Calls"):
        try:
            classification = classification_chain.invoke({
            "transcript": row["transcript"]
            })
            
            results.append({
                "call_id": row["call_id"],
                "predicted_call_type": classification.call_type,
                "confidence": classification.confidence
            })
        except Exception as e:
            print(f"Error at the row {i}: {e}")
            results.append({
                "call_id": row["call_id"],
                "predicted_call_type": None,
                "confidence": None
            })

    results_df = pd.DataFrame(results)
    transcript_df = transcript_df.merge(results_df, on="call_id")
    
    return transcript_df

#Evaluation Runner
def run_evaluation(transcript, eval_plan, tone_chain, resolution_chain, knowledge_chain):   
    results = {}
    if "tone_empathy" in eval_plan:
        try:
            tone_result = tone_chain.invoke({"transcript": transcript})
            results["tone"] = tone_result.model_dump()
        except Exception as e:
            results["tone"] = {"Error": str(e)}
            
    if "knowledge_accuracy" in eval_plan:
        try:
            knowledge_result = knowledge_chain.invoke({"transcript": transcript})
            results["knowledge"] = knowledge_result.model_dump()
        except Exception as e:
            results["knowledge"] = {"Error": str(e)}
            
    if "resolution_quality" in eval_plan:
        try:
            resolution_result = resolution_chain.invoke({"transcript": transcript})
            results["resolution"] = resolution_result.model_dump()
        except Exception as e:
            results["resolution"] = {"Error": str(e)}
            
    return results

def apply_evaluation(transcript_df, tone_chain, resolution_chain, knowledge_chain):
    evaluation_outputs = []

    for i,row in tqdm(transcript_df.iterrows(), total=len(transcript_df), desc="Running the Evaluation"):
        try:
            evaluation = run_evaluation(
                transcript=row["transcript"], 
                eval_plan=row["evaluation_plan"],
                tone_chain=tone_chain,
                resolution_chain=resolution_chain,
                knowledge_chain=knowledge_chain
                )
            evaluation_outputs.append({
                "call_id": row["call_id"],
                "evaluation_output": evaluation
            })
        except Exception as e:
            print(f"Error at the row {i}: {e}")
            evaluation_outputs.append({
                "call_id": row["call_id"],
                "evaluation_output": None
            })

    eval_df = pd.DataFrame(evaluation_outputs)
    transcript_df = transcript_df.merge(eval_df, on="call_id")
    return transcript_df

def generate_final_report(transcript_df, final_reporting_chain):
    final_outputs = []

    for i,row in tqdm(transcript_df.iterrows(), total=len(transcript_df), desc="Final Report Summary Generation"):
        try:
            result = final_reporting_chain.invoke({
                "evaluation_output": row["evaluation_output"]
            })
            final_outputs.append({
                "call_id": row["call_id"],
                "summary": result.summary,
                "recommendations": result.recommendation
            })
        except Exception as e:
            print(f"Error at row {i}: {e}")
            final_outputs.append({
                "call_id": row["call_id"],
                "summary": None,
                "recommendations": None
            })

    final_report_df = pd.DataFrame(final_outputs)
    transcript_df = transcript_df.merge(final_report_df, on="call_id")
    return transcript_df