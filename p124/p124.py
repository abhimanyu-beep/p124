from flask import Flask,request,jsonify
app=Flask(__name__)
tasks=[
    {
        "id":1,
        "title":"by the vegetables",
        "description":"potato,tomato,carrot",
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide the data"
        },400)
        task={
            "id":tasks[-1]["id"]+1,
            "title":request.json["title"],
            "description":request.json.get("description",""),
        }
        tasks.append(task)
        return jsonify({
            "status":"success",
            "message":"task added successfully"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "contact":"9987644456",
        "name":"Raju",
        "done":false,
        "id":1
    })
if(__name__=="__main__"):
    app.run(debug=True)    