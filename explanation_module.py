from transformers import pipeline

# We instantiate the pipeline lazily to avoid heavy loading if not needed.
_explanation_pipeline = None

def get_explanation_pipeline():
    global _explanation_pipeline
    if _explanation_pipeline is None:
        try:
            # We use MBZUAI/LaMini-Flan-T5-783M as specified in the SRS.
            # Using CPU for widespread compatibility, but transformers handles it automatically.
            _explanation_pipeline = pipeline(
                'text2text-generation', 
                model='MBZUAI/LaMini-Flan-T5-783M'
            )
        except Exception as e:
            raise Exception(f"Failed to load LaMini-Flan-T5 model: {str(e)}")
    return _explanation_pipeline

def explain_concept(concept: str) -> str:
    try:
        pl = get_explanation_pipeline()
        prompt = f"Explain the following concept simply for a beginner: {concept}"
        # model generates text based on prompt
        results = pl(prompt, max_length=256, do_sample=True, temperature=0.7)
        return results[0]['generated_text']
    except Exception as e:
        return f"Error occurred while generating explanation: {str(e)}"
