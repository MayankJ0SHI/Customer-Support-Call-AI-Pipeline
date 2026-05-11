from src.components.classification import get_classification_chain
from src.components.reporting import get_final_reporting_chain
from src.components.router import apply_routing
from src.components.evaluation import (
    get_knowledge_chain,
    get_resolution_chain,
    get_tone_chain
)

from src.pipeline.pipeline import (
    run_classification,
    apply_evaluation,
    generate_final_report
)

from src.utils.config_loader import load_config
from src.utils.data_loader import load_transcript
from src.utils.llm_loader import load_llm
from src.utils.helpers import save_dataframe

def main():
    
    print("\n===== 🔃 Loading the Config and Transcripts ======\n")
    config = load_config()
    transcript_df = load_transcript()
    print("Config and Transcripts are loaded successfully ✅")
    
    print("\n===== 🔃 Loading the LLM ======\n")
    llm = load_llm(config)
    print(f"Loaded the LLM {llm.__class__.__name__} successfully ✅")
    
    print("\n===== 👾 Creating the Chains ======\n")
    classification_chain = get_classification_chain(llm, config)
    tone_chain = get_tone_chain(llm)
    knowledge_chain = get_knowledge_chain(llm)
    resolution_chain = get_resolution_chain(llm)
    final_reporting_chain = get_final_reporting_chain(llm)
    print(f"Created the chains successfully ✅")
    
    print("\n====== 🅿️ Pipeline Triggerred =====\n")
    
    print("Step 1️⃣: Running the Call Type Classification\n")
    transcript_df = run_classification(transcript_df=transcript_df, classification_chain=classification_chain)
    
    print("\nStep 2️⃣: Routing to the respective call type for evaluation\n")
    transcript_df = apply_routing(transcript_df=transcript_df)
    
    print("\nStep 3️⃣: Performing the evaluation\n")
    transcript_df = apply_evaluation(
        transcript_df=transcript_df, 
        tone_chain=tone_chain, 
        resolution_chain=resolution_chain, 
        knowledge_chain=knowledge_chain
    )
    
    print("\nStep 4️⃣: Generating the final report\n")
    transcript_df = generate_final_report(transcript_df=transcript_df, final_reporting_chain=final_reporting_chain)
    
    print("\nStep 5️⃣: Saving the report\n")
    save_dataframe(transcript_df)
    
    print("\n====== 🅿️ Pipeline Executed Successfully ✅✅✅ =====\n")
    
if __name__ == "__main__":
    main()