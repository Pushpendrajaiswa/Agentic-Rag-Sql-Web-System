from graph import app

while True:
    query = input("Ask: ")

    result = app.invoke({
        "query": query
    })

    print("\nFinal Answer:\n", result["response"])