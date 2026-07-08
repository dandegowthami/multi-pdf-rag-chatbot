import {
  useState,
  useEffect
} from "react";

import API from "../../services/api";

import "./ChatSection.css";

function ChatSection({
  clearChat
}) {

  const [question, setQuestion] =
    useState("");

  const [messages, setMessages] =
    useState([]);

  useEffect(() => {

    if (clearChat) {

      setMessages([]);

      setQuestion("");
    }

  }, [clearChat]);

  const askQuestion = async () => {

    if (!question.trim()) return;

    const userMessage = {

      type: "user",

      text: question
    };

    setMessages((prev) => [

      ...prev,

      userMessage
    ]);

    try {

      const response =
        await API.post(
          "/ask",
          {
            question
          }
        );

      const botMessage = {

        type: "bot",

        answer:
          response.data.answer,

        source:
          response.data.source ||
          response.data.sources
      };

      setMessages((prev) => [

        ...prev,

        botMessage
      ]);

    } catch (error) {

      console.log(error);

      setMessages((prev) => [

        ...prev,

        {

          type: "bot",

          answer:
            "Something went wrong"
        }
      ]);
    }

    setQuestion("");
  };

  return (

    <div className="chat-container">

      <div className="chat-messages">

        {

          messages.map(

            (msg, index) => (

              <div
                key={index}
                className={
                  msg.type === "user"
                    ? "user-msg"
                    : "bot-msg"
                }
              >

                {

                  msg.type === "user"

                    ? (

                      <p>
                        {msg.text}
                      </p>

                    )

                    : (

                      <>

                        <p>
                          {msg.answer}
                        </p>
                      </>
                    )
                }

              </div>
            )
          )
        }

      </div>

      <div className="chat-input">

        <input

          type="text"

          placeholder="Ask something..."

          value={question}

          onChange={(e) =>
            setQuestion(
              e.target.value
            )
          }

          onKeyDown={(e) => {

            if (
              e.key === "Enter"
            ) {

              askQuestion();
            }
          }}

        />

        <button
          onClick={askQuestion}
        >
          Send
        </button>

      </div>

    </div>

  );
}

export default ChatSection;