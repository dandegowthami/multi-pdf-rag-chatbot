import {
  useState,
  useEffect
} from "react";

import API from "../../services/api";

import "./UploadSection.css";

function UploadSection() {

  const [file, setFile] = useState(null);

  const [message, setMessage] =
    useState("");

  const [documents, setDocuments] =
    useState([]);

  const fetchDocuments = async () => {

    try {

      const response =
        await API.get(
          "/documents"
        );

      setDocuments(
        response.data.documents
      );

    } catch (error) {

      console.log(error);
    }
  };

  useEffect(() => {

    fetchDocuments();

  }, []);

  const uploadPDF = async () => {

    if (!file) return;

    const formData =
      new FormData();

    formData.append(
      "file",
      file
    );

    try {

      const response =
        await API.post(
          "/upload",
          formData
        );

      setMessage(
        response.data.status
      );

      fetchDocuments();

      setFile(null);

    } catch (error) {

      console.log(error);

      setMessage(
        "Upload Failed"
      );
    }
  };

  const deleteDocument = async (
    pdfName
  ) => {

    try {

      await API.delete(
        `/document/${pdfName}`
      );

      fetchDocuments();

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="upload-container">

      <h3>
        Upload PDF Document
      </h3>

      <div className="upload-box">

        <input
          type="file"
          accept=".pdf"
          onChange={(e) =>
            setFile(
              e.target.files[0]
            )
          }
        />

        <button
          onClick={uploadPDF}
        >
          Upload PDF
        </button>

      </div>

      {message && (

        <p className="message">

          {message}

        </p>

      )}

      <div className="documents-section">

        <h4>
          Uploaded Documents
        </h4>

        {

          documents.length === 0

          ?

          <p>
            No documents uploaded
          </p>

          :

          documents.map(
            (doc, index) => (

              <div
                key={index}
                className="document-card"
              >

                <span>

                  📄 {doc}

                </span>

                <button
                  className="delete-btn"
                  onClick={() =>
                    deleteDocument(doc)
                  }
                >

                  Delete

                </button>

              </div>

            )
          )
        }

      </div>

    </div>

  );
}

export default UploadSection;