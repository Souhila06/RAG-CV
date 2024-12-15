from LLM.controller import Controller
from pathlib import Path
import PyPDF2

def get_text_from_pdfs():
    # Path de tous les CVs (documents PDF qui se trouvent dans ./CVs/) potentiellement à changer si on veut plus de flexibilité
    pdf_paths = [p for p in Path("./CVs").iterdir() if p.is_file() and p.suffix.lower() == '.pdf']
    
    full_text = []
    
    #Process de tous les paths
    for pdf_path in pdf_paths:
        try:
            with open(pdf_path, 'rb') as file:
                #Lecture du PDF
                reader = PyPDF2.PdfReader(file)
                
                # Extraction du texte
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                
                full_text.append(text)
                
        except Exception as e:
            print(f"Error processing {pdf_path}: {str(e)}")
    
    # Liste du contenu de chaque PDF
    return full_text


if __name__ == '__main__':

    full_text = get_text_from_pdfs()

    #On enlève les retours à la ligne -> sinon mauvaise génération
    for i in range(len(full_text)):
        full_text[i] = full_text[i].replace('\n', '   ')
        
    #Requête utilisateur
    query = input("\nPrompt : \n")

    #Instanciation du LLM et génération de la réponse
    controller = Controller()
    output = controller.generate_response(query, full_text)

    #Streaming : output est un générateur (yield), on affiche chaque token au fur et à mesure
    for token in output:
        print(token['choices'][0]['text'], end='', flush=True)
