import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { motion } from "framer-motion";

const elements = [
  { name: "Hidrógeno", symbol: "H", atomicNumber: 1, config: "1s1" },
  { name: "Helio", symbol: "He", atomicNumber: 2, config: "1s2" },
  { name: "Litio", symbol: "Li", atomicNumber: 3, config: "1s2 2s1" },
  { name: "Berilio", symbol: "Be", atomicNumber: 4, config: "1s2 2s2" },
  { name: "Boro", symbol: "B", atomicNumber: 5, config: "1s2 2s2 2p1" },
];

export default function ElectronConfigurationGame() {
  const [currentElement, setCurrentElement] = useState(null);
  const [userInput, setUserInput] = useState("");
  const [feedback, setFeedback] = useState("");

  useEffect(() => {
    getRandomElement();
  }, []);

  const getRandomElement = () => {
    const randomIndex = Math.floor(Math.random() * elements.length);
    setCurrentElement(elements[randomIndex]);
    setUserInput("");
    setFeedback("");
  };

  const checkAnswer = () => {
    if (userInput.trim() === currentElement.config) {
      setFeedback("✅ ¡Correcto!");
    } else {
      setFeedback("❌ Incorrecto. Inténtalo de nuevo.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Card className="p-6 shadow-xl rounded-2xl bg-white">
          <CardContent className="flex flex-col items-center">
            <h2 className="text-xl font-bold mb-4">{currentElement?.name} ({currentElement?.symbol})</h2>
            <p className="mb-4">Número Atómico: {currentElement?.atomicNumber}</p>
            <Input
              value={userInput}
              onChange={(e) => setUserInput(e.target.value)}
              placeholder="Ingresa la configuración electrónica"
              className="mb-4 text-center"
            />
            <Button onClick={checkAnswer} className="mb-2">Verificar</Button>
            <p className="text-lg font-semibold">{feedback}</p>
            <Button onClick={getRandomElement} className="mt-4">Siguiente</Button>
          </CardContent>
        </Card>
      </motion.div>
    </div>
  );
}
