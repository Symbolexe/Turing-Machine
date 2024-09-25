# GitHub Link : https://github.com/symbolexe
try:
    import string
    import argparse
    alphabet = string.ascii_uppercase
    class EnigmaMachine:
        def __init__(self, rotors, reflector, plugboard=None, ring_settings=None):
            self.rotors = rotors
            self.reflector = reflector
            self.plugboard = plugboard if plugboard else {}
            self.rotor_positions = [0] * len(rotors)
            self.ring_settings = ring_settings if ring_settings else [0] * len(rotors)
            self.notch_positions = [rotor['notch'] for rotor in rotors]
        def set_rotor_positions(self, positions):
            self.rotor_positions = positions
        def step_rotors(self):
            self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
            if self.rotor_positions[0] == self.notch_positions[0]:
                self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26
            if self.rotor_positions[1] == self.notch_positions[1]:
                self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26
        def swap_plugboard(self, letter):
            return self.plugboard.get(letter, letter)
        def pass_through_rotor(self, letter, rotor, position, ring_setting, reverse=False):
            offset = (position - ring_setting) % 26
            if not reverse:
                index = (alphabet.index(letter) + offset) % 26
                return rotor['mapping'][index]
            else:
                index = rotor['mapping'].index(letter)
                return alphabet[(index - offset) % 26]
        def reflector_encode(self, letter):
            index = alphabet.index(letter)
            return self.reflector[index]
        def encode_letter(self, letter):
            self.step_rotors()
            letter = self.swap_plugboard(letter)
            for i in range(len(self.rotors)):
                letter = self.pass_through_rotor(
                    letter, self.rotors[i], self.rotor_positions[i], self.ring_settings[i])
            letter = self.reflector_encode(letter)
            for i in reversed(range(len(self.rotors))):
                letter = self.pass_through_rotor(
                    letter, self.rotors[i], self.rotor_positions[i], self.ring_settings[i], reverse=True)
            return self.swap_plugboard(letter)
        def encode_message(self, message):
            encoded_message = []
            for letter in message.upper():
                if letter in alphabet:
                    encoded_message.append(self.encode_letter(letter))
                else:
                    encoded_message.append(letter)
            return ''.join(encoded_message)
    def main():
        parser = argparse.ArgumentParser(description='Enigma Machine Encoder/Decoder')
        parser.add_argument('--encode', type=str, help='Text to encode')
        parser.add_argument('--decode', type=str, help='Text to decode')
        parser.add_argument('--rotor_positions', nargs=3, type=int, required=True, help='Rotor positions (e.g., 0 1 2)')
        parser.add_argument('--ring_settings', nargs=3, type=int, required=True, help='Ring settings (e.g., 1 2 3)')
        parser.add_argument('--plugboard', nargs='*', help='Plugboard configuration (e.g., A-B C-D)')
        args = parser.parse_args()
        if not args.encode and not args.decode:
            print("Please provide either --encode or --decode option.")
            return
        rotor_I = {'mapping': "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'notch': 16}
        rotor_II = {'mapping': "AJDKSIRUXBLHWTMCQGZNPYFVOE", 'notch': 4}
        rotor_III = {'mapping': "BDFHJLCPRTXVZNYEIWGAKMUSQO", 'notch': 21}
        reflector_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        plugboard_config = {}
        if args.plugboard:
            for pair in args.plugboard:
                letter1, letter2 = pair.split('-')
                plugboard_config[letter1] = letter2
                plugboard_config[letter2] = letter1
        enigma = EnigmaMachine([rotor_I, rotor_II, rotor_III], reflector_B, plugboard_config, args.ring_settings)
        enigma.set_rotor_positions(args.rotor_positions)

        if args.encode:
            result = enigma.encode_message(args.encode)
            print(f"Encoded message: {result}")
        elif args.decode:
            result = enigma.encode_message(args.decode)
            print(f"Decoded message: {result}")
    if __name__ == "__main__":
        main()
except Exception as e:
    print(e)