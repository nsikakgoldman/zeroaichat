import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def aiResponse():
  resp = """
  Lagos is a bustling city located in southwest Nigeria, positioned along the country's Atlantic coast. It is the largest city in Nigeria and one of the fastest-growing cities in Africa. Named after the Portuguese word for "lakes," Lagos is historically known for its lagoons and waterways. Lagos has a vibrant and diverse culture, influenced by various ethnic groups such as the Yoruba, Igbo, and Hausa. This rich cultural tapestry is evident in the city's art, music, food, and traditional festivals, which attract both locals and tourists. The city is a major economic hub and a significant financial center in Africa. It is home to the Nigerian Stock Exchange, many national and multinational corporations, and an active entrepreneurial scene. This economic growth has also led to an emerging middle class, which has contributed to the city's rapid urbanization and modernization. Lagos is famous for its lively markets, where you can find a wide range of goods, from unique crafts and fabrics to fresh produce and food items. The city is renowned for its street food, with dishes like jollof rice, suya (grilled meat skewers), and puff puff (a type of fried dough) being local favorites. In terms of landmarks, Lagos offers a mix of modern architecture and historical sites. Prominent attractions include the National Museum of Nigeria, Lekki Conservation Centre, Nike Art Gallery, Tafawa Balewa Square, and the iconic Third Mainland Bridge, one of the longest bridges in Africa. However, Lagos faces some challenges as well, such as traffic congestion, rapid urbanization, and inadequate infrastructure in some areas. Efforts are being made to address these issues and improve the quality of life for residents. Overall, Lagos is a vibrant, dynamic, and culturally diverse city with a lot to offer. Its bustling markets, rich cultural heritage, and economic opportunities make it a fascinating place to visit or live in.
  """
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      # prompt= "tell me about... lagos"
      messages=[
      {"role": "system", "content": f"You are a helpful assistant.and you answered {resp}"},
      {"role": "user", "content": "why  It is home to the Nigerian Stock Exchange"}
    ]
  )
  # print(completion['choices'][0]['message']['content'])
  return str(completion.choices[0].message.content)

# print(completion.choices)
# print(completion.choices[0].message)