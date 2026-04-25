import { useEffect, useState } from "react";
import Webcam from "react-webcam";

const emojiMap = {
  thumbs_up: "👍",
  stop: "✋",
  victory: "✌️",
  fist: "👊",
  one: "☝️",
  point_right: "👉",
  neutral: "😐",
  error: "⚠️"
};

function App() {
  const [gesture, setGesture] = useState("neutral");
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/gesture");
        const data = await res.json();

        setGesture(data.gesture);
        setConnected(true);
      } catch {
        setConnected(false);
      }
    }, 300);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="h-screen bg-gradient-to-br from-black via-gray-900 to-gray-800 flex items-center justify-center text-white">

      <div className="flex gap-10 items-center">

        {/* Webcam */}
        <div className="rounded-3xl overflow-hidden border border-white/20 shadow-2xl">
          <Webcam
            audio={false}
            screenshotFormat="image/jpeg"
            className="w-[400px] h-[300px] object-cover"
          />
        </div>

        {/* UI Panel */}
        <div className="w-[350px] p-8 rounded-3xl bg-white/10 backdrop-blur-xl border border-white/20 shadow-2xl text-center">

          <h1 className="text-2xl font-bold mb-4">
            ✋ Gesture AI
          </h1>

          {/* Status */}
          <div className="flex items-center justify-center gap-2 mb-6">
            <div className={`w-3 h-3 rounded-full ${connected ? "bg-green-400" : "bg-red-500"} animate-pulse`} />
            <span className="text-sm">
              {connected ? "Connected" : "Disconnected"}
            </span>
          </div>

          {/* Gesture Display */}
          <div className="bg-black/40 rounded-2xl p-6 shadow-inner">

            <div className="text-6xl mb-3 animate-bounce">
              {emojiMap[gesture] || "❓"}
            </div>

            <h2 className="text-2xl font-bold text-green-400 capitalize">
              {gesture}
            </h2>

          </div>

          <p className="mt-6 text-xs text-gray-400">
            Real-time AI detection
          </p>

        </div>

      </div>
    </div>
  );
}

export default App;