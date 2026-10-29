import gradio as gr
from spam_sheild import classify,explain
def check(message):
    flagged = ", ".join(explain(message))
    return classify(message), flagged
demo = gr.interface(
        fn = check,
        input = gr.Textbox(lines=3,label="enter a msg"),
        output=[
            gr.Textbox(lables="result"),
            gr.text(lable = "spam words found")
        ],
        title = "spam shield",
        description="Check whether a message is SPAM or SAFE.",
        examples=[  
            ["Congratulations! You won a free prize"],
            ["Hey, how are you?"],
            ["Urgent! Verify your account"]
        ]
)
if __name__=="__main__":
    demo.launch()