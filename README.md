# Turing-Machine
![3 2@2x](https://github.com/user-attachments/assets/b68b4bc1-9a2f-406b-a447-da1b6705cfdb)
## Enigma Machine and Cracker Tool
### Overview
This tool is a fully functional simulation of the Enigma Machine, an encryption device used by Nazi Germany during World War II to encrypt military communications. The Enigma Machine was famous for its complexity and perceived unbreakability, but thanks to the work of mathematicians like Alan Turing, the cipher was eventually cracked, leading to significant contributions to the Allied victory.

The Enigma Machine and Cracker Tool allows users to:

1. Encrypt and Decrypt messages using a simulation of the original Enigma Machine.
2. Crack Enigma-encrypted messages using both brute force and known plaintext attacks, just like in the historical efforts of codebreaking at Bletchley Park.
![1 2@2x](https://github.com/user-attachments/assets/fd4bbfe7-175d-4590-bd42-c1c0becb5df5)

This tool is designed to be easy to use, powerful, and accurate to the real workings of the Enigma Machine, making it ideal for enthusiasts, students, or anyone interested in cryptography.

### Key Features
The ```Machine.py``` script simulates the inner workings of the Enigma Machine and provides an interface for both encoding and decoding messages. This includes the historically accurate simulation of:
- [x] Rotor Settings: Supports multiple rotors, each with unique wiring configurations and notches for stepping.
- [x] Rotor Stepping Mechanism: Implements the double-stepping behavior, where rotors rotate in sequence, mimicking the real Enigma machine’s movement.
- [x] Ring Settings: Allows the user to adjust the ring settings for each rotor, which changes the rotor’s relative alignment to the alphabet, adding another layer of encryption.
- [x] Plugboard Configuration: The plugboard allows for letter substitution before and after the rotors, further scrambling the input.
- [x] Reflector: Just like the real Enigma machine, the reflector reverses the signal back through the rotors.

With this tool, you can simulate the entire Enigma encryption/decryption process with customizable configurations.
### Command-Line Usage
#### Brute-Force Cracking (No Known Phrases)
```bash
python Cracker.py --crack "Encrypted message"
```

The tool will attempt every possible rotor combination to decode the message and output the results in real-time.

![4@2x](https://github.com/user-attachments/assets/2b0a65b7-cf76-4a38-9c88-6e73d8cf7385)

#### Cracking with Known Phrases
```bash
python Cracker.py --crack "Encrypted message here" --possible "known phrase" "another phrase"
```
The tool will use the provided known phrases to assist the cracking process, looking for matches as it tests rotor combinations.

![2 2@2x](https://github.com/user-attachments/assets/19284858-e15d-427b-b543-cff19cf9caa4)

### Technical Features and Realism
1. Rotor Mechanism: Implements three rotors with the correct wiring configurations and notch stepping. Each rotor rotates after a letter is encoded, and the second and third rotors step according to the Enigma machine’s double-stepping mechanism.
2. Reflector: The signal passes through the reflector, bouncing back through the rotors, accurately simulating the real-life encryption process.
3. Plugboard: The plugboard adds an additional layer of letter substitution both before and after the rotors, just like in the historical Enigma machine. The user can define pairs of letters to be swapped during encryption.
4. Brute-Force Cracking: The tool simulates the exhaustive process of testing all rotor positions, ring settings, and rotor orders—a method that was famously used at Bletchley Park to crack intercepted Enigma messages.
5. Known Plaintext Cracking: In real-world codebreaking, cryptanalysts used known phrases (such as “weather report”) to quickly spot possible configurations. This tool replicates that method, letting you provide known plaintext fragments to narrow down the search space and identify the correct rotor settings faster.

### Usage Examples
Here are some examples of how to use this tool.
#### Encrypting a Message
```bash
python Machine.py --encode "HELLO YASIN" --rotor_positions 0 1 2 --ring_settings 1 2 3 --plugboard A-B C-D
```
#### Decrypting a Message
```bash
python Machine.py --decode "UOEGI OHVWB" --rotor_positions 0 1 2 --ring_settings 1 2 3 --plugboard A-B C-D
```
#### Cracking an Encrypted Message (Brute Force)
```bash
python Cracker.py --crack "UOEGI OOVWA"
```
#### Cracking with Known Phrases
```bash
python Cracker.py --crack "UOEGI OOVWA" --possible "hello" "yasin"
```
## Conclusion
This Enigma Machine and Cracker Tool is not only a tribute to one of the most famous cryptographic devices in history but also a fully functional tool that allows you to encode, decode, and crack Enigma-encrypted messages just as they did at Bletchley Park. Whether you’re a student of history, a cryptography enthusiast, or just curious about how the Enigma machine worked, this tool gives you a hands-on experience.
