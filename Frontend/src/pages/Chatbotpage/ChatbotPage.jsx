import { useState } from "react";

import UploadSection from "../../components/UploadSection/UploadSection";
import ChatSection from "../../components/ChatSection/ChatSection";

import "./Chatbotpage.css";

function ChatbotPage() {

  const [clearChat, setClearChat] =
    useState(false);

  const handleNewChat = () => {

    const confirmChat = window.confirm(
      "Start a new chat?"
    );

    if (!confirmChat) return;

    setClearChat(true);

    setTimeout(() => {

      setClearChat(false);

    }, 100);
  };

  return (

    <div className="chatbot-page">

      <div className="top-bar">

        <div>

          <h2>
            RAG Chatbot
          </h2>

          <span>
            Multi PDF Assistant
          </span>

        </div>

        <button
          onClick={handleNewChat}
        >
          New Chat
        </button>

      </div>

      <UploadSection />

      <ChatSection
        clearChat={clearChat}
      />

    </div>

  );
}

export default ChatbotPage;