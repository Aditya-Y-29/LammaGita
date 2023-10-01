from langchain.llms import CTransformers

def build_llm():
    MODEL_BIN_PATH='Models/llama-2-7b.ggmlv3.q4_0.bin'
    MODEL_TYPE='llama'
    MAX_NEW_TOKENS=512
    TEMPERATURE=0.01
    # Local CTransformers model
    llm = CTransformers(model=MODEL_BIN_PATH,
                        model_type=MODEL_TYPE,
                        config={'max_new_tokens': MAX_NEW_TOKENS,
                                'temperature': TEMPERATURE}
                        )

    return llm