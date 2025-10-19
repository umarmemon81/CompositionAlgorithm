"use client";

import { useState } from "react";
import {
  Upload,
  Play,
  FileJson,
  CheckCircle,
  AlertCircle,
  Loader,
  X,
  Download,
  Eye,
} from "lucide-react";
import axios from "axios";

export default function Home() {
  const [files, setFiles] = useState({
    availableInputs: null,
    models: null,
    compositionRequirements: null,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [modalOpen, setModalOpen] = useState(null); // 'console' or 'json'

  const handleFileChange = (key, file) => {
    setFiles((prev) => ({ ...prev, [key]: file }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (
      !files.availableInputs ||
      !files.models ||
      !files.compositionRequirements
    ) {
      setError("Please select all 3 JSON files");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const formData = new FormData();
      formData.append("files", files.availableInputs, "available_inputs.json");
      formData.append("files", files.models, "models.json");
      formData.append(
        "files",
        files.compositionRequirements,
        "compositionRequirements.json"
      );

      const response = await axios.post(
        "http://localhost:8000/api/execute",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      if (response.data.success) {
        setResult(response.data);
      } else {
        setError(response.data.error || "Unknown error occurred");
      }
    } catch (err) {
      setError("Failed to connect to the server");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const allFilesSelected =
    files.availableInputs && files.models && files.compositionRequirements;

  const downloadConsoleOutput = () => {
    const blob = new Blob([result.console_output], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "console_output.txt";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const downloadJSON = () => {
    const blob = new Blob([JSON.stringify(result, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "response.json";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="container mx-auto p-6 lg:p-8">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-slate-800 mb-2">
            Model Composition System
          </h1>
          <p className="text-slate-600">
            Upload your JSON files and execute the composition algorithm
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-6">
          {/* LEFT SIDE - INPUTS */}
          <div className="space-y-6">
            <div className="bg-white rounded-xl shadow-lg border border-slate-200 overflow-hidden">
              <div className="bg-blue-600 p-4">
                <h2 className="text-xl font-semibold text-white flex items-center gap-2">
                  <Upload className="w-5 h-5" />
                  Input Files
                </h2>
              </div>

              <form onSubmit={handleSubmit} className="p-6">
                <div className="space-y-4">
                  <FileInput
                    label="Available Inputs"
                    icon={<FileJson className="w-4 h-4" />}
                    onChange={(file) =>
                      handleFileChange("availableInputs", file)
                    }
                    accept=".json"
                    file={files.availableInputs}
                  />

                  <FileInput
                    label="Models"
                    icon={<FileJson className="w-4 h-4" />}
                    onChange={(file) => handleFileChange("models", file)}
                    accept=".json"
                    file={files.models}
                  />

                  <FileInput
                    label="Composition Requirements"
                    icon={<FileJson className="w-4 h-4" />}
                    onChange={(file) =>
                      handleFileChange("compositionRequirements", file)
                    }
                    accept=".json"
                    file={files.compositionRequirements}
                  />
                </div>

                {error && (
                  <div className="mt-4 p-4 bg-red-50 border-l-4 border-red-500 rounded-r">
                    <div className="flex items-start gap-2">
                      <AlertCircle className="w-5 h-5 text-red-600 mt-0.5 flex-shrink-0" />
                      <p className="text-red-700 text-sm">{error}</p>
                    </div>
                  </div>
                )}

                <button
                  type="submit"
                  disabled={loading || !allFilesSelected}
                  className="cursor-pointer mt-6 w-full bg-blue-600 text-white py-3 px-6 rounded-lg hover:from-blue-700 hover:to-indigo-700 disabled:from-slate-300 disabled:to-slate-400 disabled:cursor-not-allowed font-semibold shadow-lg transition-all duration-200 flex items-center justify-center gap-2 group"
                >
                  {loading ? (
                    <>
                      <Loader className="w-5 h-5 animate-spin" />
                      Processing...
                    </>
                  ) : (
                    <>
                      <Play className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                      Execute Algorithm
                    </>
                  )}
                </button>
              </form>
            </div>
          </div>

          {/* RIGHT SIDE - OUTPUTS */}
          <div className="space-y-4">
            {result ? (
              <>
                {/* Success Badge */}
                <div className="bg-green-600 rounded-xl shadow-lg p-4 text-white">
                  <div className="flex items-center gap-6">
                    <CheckCircle className="w-10 h-10" />

                    <div>
                      <h2 className="text-2xl font-bold">Results</h2>
                      <p className="text-green-100 text-sm">
                        {result.total_compositions} valid compositions found
                      </p>
                    </div>
                  </div>
                </div>

                {/* Compositions */}
                {result.solutions && result.solutions.length > 0 && (
                  <div className="bg-white rounded-xl shadow-lg border border-slate-200">
                    <div className="bg-blue-600 p-4 flex items-center justify-between">
                      <h3 className="font-semibold text-white text-lg">
                        Compositions ({result.solutions.length})
                      </h3>
                    </div>
                    <div className="p-4 space-y-3 max-h-[500px] overflow-y-auto">
                      {result.solutions.map((solution, index) => (
                        <div
                          key={index}
                          className="p-4 bg-blue-50 rounded-lg border border-blue-200 hover:border-blue-300 transition-colors"
                        >
                          <p className="font-semibold text-slate-700 mb-3 text-sm">
                            Composition {index + 1}
                          </p>
                          <div className="flex flex-wrap items-center gap-2">
                            {solution.map((m, i) => (
                              <div key={i} className="flex items-center gap-2">
                                <span className="bg-white px-3 py-1.5 rounded-lg text-sm font-medium text-slate-700 shadow-sm border border-slate-200 hover:shadow-md transition-shadow">
                                  {m.name}
                                </span>
                                {i < solution.length - 1 && (
                                  <span className="text-blue-400 font-bold">
                                    →
                                  </span>
                                )}
                              </div>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Console Output */}
                <div className="bg-white rounded-xl shadow-lg border border-slate-200">
                  <div className="bg-slate-800 p-4 flex items-center justify-between rounded-t-xl">
                    <h3 className="font-semibold text-white text-lg">
                      Console Output
                    </h3>
                    <button
                      onClick={() => setModalOpen("console")}
                      className="cursor-pointer flex items-center gap-2 bg-slate-700 hover:bg-slate-600 text-white px-3 py-2 rounded-lg text-sm font-medium transition-colors"
                    >
                      <Eye className="w-4 h-4" />
                      Full View
                    </button>
                  </div>
                  <div className="p-4">
                    <pre className="bg-slate-900 text-green-400 p-4 rounded-lg overflow-auto max-h-60 text-xs font-mono">
                      {result.console_output}
                    </pre>
                  </div>
                </div>

                {/* JSON Response */}
                <div className="bg-white rounded-xl shadow-lg border border-slate-200">
                  <div className="bg-slate-100 p-4 flex items-center justify-between rounded-t-xl">
                    <h3 className="font-semibold text-slate-800 text-lg">
                      Raw JSON Response
                    </h3>
                    <button
                      onClick={() => setModalOpen("json")}
                      className="cursor-pointer flex items-center gap-2 bg-slate-700 hover:bg-slate-600 text-white px-3 py-2 rounded-lg text-sm font-medium transition-colors"
                    >
                      <Eye className="w-4 h-4" />
                      Full View
                    </button>
                  </div>
                  <div className="p-4">
                    <pre className="bg-slate-50 text-slate-900 p-4 rounded-lg overflow-auto max-h-60 text-xs font-mono border border-slate-200">
                      {JSON.stringify(result, null, 2)}
                    </pre>
                  </div>
                </div>
              </>
            ) : (
              <div className="bg-white rounded-xl shadow-lg border border-slate-200 p-12 text-center">
                <div className="w-16 h-16 bg-slate-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <FileJson className="w-8 h-8 text-slate-400" />
                </div>
                <h3 className="text-lg font-semibold text-slate-700 mb-2">
                  No Results Yet
                </h3>
                <p className="text-slate-500">
                  Upload your files and execute the algorithm to see results
                  here
                </p>
              </div>
            )}
          </div>
        </div>

        {/* Preview Modal */}
        {modalOpen && (
          <div className="fixed inset-0 backdrop-blur-sm bg-opacity-50 flex items-center justify-center z-50 p-4 shadow-2xl">
            <div className="bg-white rounded-xl shadow-2xl max-w-4xl w-full max-h-[90vh] flex flex-col">
              {/* Modal Header */}
              <div className="flex items-center justify-between p-6 border-b border-slate-200">
                <h3 className="text-2xl font-bold text-slate-800">
                  {modalOpen === "console"
                    ? "Console Output Preview"
                    : "JSON Response Preview"}
                </h3>
                <div className="flex items-center gap-2">
                  <button
                    onClick={
                      modalOpen === "console"
                        ? downloadConsoleOutput
                        : downloadJSON
                    }
                    className="cursor-pointer flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium transition-colors"
                  >
                    <Download className="w-4 h-4" />
                    Download
                  </button>
                  <button
                    onClick={() => setModalOpen(null)}
                    className="cursor-pointer p-2 hover:bg-slate-100 rounded-lg transition-colors"
                  >
                    <X className="w-6 h-6 text-slate-600" />
                  </button>
                </div>
              </div>

              {/* Modal Content */}
              <div className="flex-1 overflow-auto p-6">
                <pre
                  className={`${
                    modalOpen === "console"
                      ? "bg-slate-900 text-green-400"
                      : "bg-slate-50 text-slate-900"
                  } p-4 rounded-lg text-sm font-mono overflow-auto`}
                >
                  {modalOpen === "console"
                    ? result.console_output
                    : JSON.stringify(result, null, 2)}
                </pre>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function FileInput({ label, icon, onChange, accept, file }) {
  return (
    <div>
      <label className="text-sm font-semibold text-slate-700 mb-2 flex items-center gap-2">
        {icon}
        {label}
      </label>
      <div className="relative">
        <input
          type="file"
          accept={accept}
          onChange={(e) => onChange(e.target.files?.[0] || null)}
          className="block w-full text-sm text-slate-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-100 file:text-blue-700 hover:file:bg-blue-200 file:cursor-pointer cursor-pointer border border-slate-300 rounded-lg bg-white hover:border-blue-400 transition-colors"
        />
        {file && (
          <div className="mt-2 text-xs text-green-600 flex items-center gap-1">
            <CheckCircle className="w-3 h-3" />
            {file.name}
          </div>
        )}
      </div>
    </div>
  );
}
