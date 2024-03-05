import json
from googletrans import Translator  # Reemplaza esto con tu método preferido de traducción

def translate_to_french(text):
    # Aquí puedes usar tu propio método de traducción o una API de traducción
    translator = Translator()
    translation = translator.translate(text, src='en', dest='fr')
    return translation.text

def translate_json_to_french(input_json, output_json):
    with open(input_json, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        # Traduce todos los campos de texto en el JSON
        translated_data = recursive_translate(data)

    # Escribe el JSON traducido en un nuevo archivo
    with open(output_json, 'w', encoding='utf-8') as json_out:
        json.dump(translated_data, json_out, ensure_ascii=False, indent=4)

    print(f'Archivo traducido creado: {output_json}')

def recursive_translate(data):
    if isinstance(data, dict):
        translated_dict = {}
        for key, value in data.items():
            translated_key = translate_to_french(key)
            if isinstance(value, (dict, list)):
                translated_value = recursive_translate(value)
            else:
                translated_value = translate_to_french(value)
            translated_dict[translated_key] = translated_value
        return translated_dict
    elif isinstance(data, list):
        translated_list = []
        for item in data:
            translated_list.append(recursive_translate(item))
        return translated_list
    else:
        return data

# Ejemplo de uso:
if __name__ == "__main__":
    input_json_file = 'input_data.json'  # Nombre del archivo JSON de entrada
    output_json_file = 'translated_data.json'  # Nombre del archivo JSON de salida
    translate_json_to_french(input_json_file, output_json_file)
