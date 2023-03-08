#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @VysakhTG

import openai

async def ai(query):
    openai.api_key = "abcd" #get this value from https://beta.openai.com/.
    engine = "davinci-codex" #change as your wish 
    response = openai.Completion.create(engine=engine, prompt=query, max_tokens=1024, n=1, stop=None, temperature=0.5, timeout=5)
    return response.choices[0].text.strip()

async def ask_ai(client, m, message):
    try:
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f"👉 User: {message.from_user.mention}\n👉 Query: {question}\n\n📝 Answer:\n\n{response}")
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)
