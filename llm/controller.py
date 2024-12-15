from llama_cpp import Llama


class Controller:
    def __init__(self, temperature, max_tokens):
        self.llm = Llama(
            # model_path="./LLM/Mistral-Nemo-Base-2407.i1-Q4_K_S.gguf",
            model_path="./LLM/qwen2.5-1.5b-instruct-q8_0.gguf",
            n_gpu_layers=-1,
            n_ctx=10000,
            verbose=False,
            offload_kqv=True,
        )
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate_response(self, query, documents):
        # Aggrégation des CVs, potentiellement à adapter à l'input
        input = ""
        for i in range(len(documents)):
            input += "Document " + str(i) + ": " + documents[i] + "\n"

        # Génération de l'output
        output = self.llm(
            "You are an expert in editing CVs. Here are the CVs:\n\nContext : " + input + " Query: " + query + " Answer: ",
            max_tokens=self.max_tokens,
            stop=["Context", "Q:", "</s>", "---"],
            echo=False,
            temperature=self.temperature,
            top_k=40,
            stream=True,
            repeat_penalty=1.1,
        )

        return output
