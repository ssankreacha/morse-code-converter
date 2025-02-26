# 🔠 Morse Code Converter (Python)

## 📌 Overview
The **Morse Code Converter** is a Python-based command-line application that **converts English text into Morse code**.  
It supports **letters (A-Z), numbers (0-9), common symbols (, . ? / - ( ) ), and spaces (represented as `/`).**  

This project demonstrates:
- **Dictionary-based encoding** for fast lookups
- **Handling of invalid characters** (ignores unsupported input)
- **Pythonic `.get()` method** for clean, efficient error handling

---

## 🚀 Features
✅ **Converts Text to Morse Code** (Letters, numbers, basic symbols)  
✅ **Ignores Unsupported Characters** (Prevents crashes)  
✅ **Handles Spaces Between Words** (`' '` → `'/'`)  
✅ **Case Insensitive** (Handles lowercase and uppercase input)  

---

## 🏗️ How It Works

### **1️⃣ User Input**
- Enter any text (letters, numbers, basic punctuation)
- Spaces are automatically converted to `/` in Morse code

### **2️⃣ Conversion Logic**
- The program loops through the input and converts each character  
- Uses a **dictionary (`MORSE_CODE_DICT`)** for fast lookup  
- **Ignores unknown characters** gracefully

### **3️⃣ Output**
- Displays both the **original text** and the **Morse code** equivalent

---

## 🛠️ Technologies Used
- ✅ Python 3+ – Core logic
- ✅ Dictionary-based Encoding – Fast lookup for conversion
- ✅ Exception Handling – Prevents errors with .get() method

---

## 🔮 Future Enhancements
- 🚀 Add Reverse Conversion (Morse Code → Text)
- 🚀 GUI Version with Tkinter (User-friendly interface)
- 🚀 File Input/Output Support (Read text files & output Morse code)