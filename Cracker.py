# GitHub Link : https://github.com/symbolexe
try:
    import argparse
    import string
    from Machine import EnigmaMachine
    def brute_force_cracker(encoded_message, enigma_machine, rotor_order_combinations):
        print("Brute forcing without known plaintext possibilities...")
        for rotor_order in rotor_order_combinations:
            enigma_machine.rotors = rotor_order
            for r1 in range(26):
                for r2 in range(26):
                    for r3 in range(26):
                        for ring1 in range(26):
                            for ring2 in range(26):
                                for ring3 in range(26):
                                    enigma_machine.set_rotor_positions([r1, r2, r3])
                                    enigma_machine.ring_settings = [ring1, ring2, ring3]
                                    decoded_message = enigma_machine.encode_message(encoded_message)
                                    print(f"Trying rotors {r1}, {r2}, {r3}, Rings {ring1}, {ring2}, {ring3}: {decoded_message}")
        return None
    def possibility_based_cracker(encoded_message, possibilities, enigma_machine, rotor_order_combinations):
        print("Cracking with known possibilities...")
        for rotor_order in rotor_order_combinations:
            enigma_machine.rotors = rotor_order
            for r1 in range(26):
                for r2 in range(26):
                    for r3 in range(26):
                        for ring1 in range(26):
                            for ring2 in range(26):
                                for ring3 in range(26):
                                    enigma_machine.set_rotor_positions([r1, r2, r3])
                                    enigma_machine.ring_settings = [ring1, ring2, ring3]
                                    decoded_message = enigma_machine.encode_message(encoded_message)
                                    for possibility in possibilities:
                                        if possibility.upper() in decoded_message:
                                            print(f"Match found! Rotors {r1}, {r2}, {r3}, Rings {ring1}, {ring2}, {ring3}: {decoded_message}")
                                            return decoded_message
                                    print(f"Trying rotors {r1}, {r2}, {r3}, Rings {ring1}, {ring2}, {ring3}: {decoded_message}")

        return None
    def main():
        parser = argparse.ArgumentParser(description='Enigma Machine Cracker')
        parser.add_argument('--crack', type=str, required=True, help='Encoded text to crack')
        parser.add_argument('--possible', nargs='*', help='Possible plaintext fragments to assist cracking (optional)')
        args = parser.parse_args()
        encoded_message = args.crack.upper()
        rotor_I = {'mapping': "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'notch': 16}
        rotor_II = {'mapping': "AJDKSIRUXBLHWTMCQGZNPYFVOE", 'notch': 4}
        rotor_III = {'mapping': "BDFHJLCPRTXVZNYEIWGAKMUSQO", 'notch': 21}
        reflector_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        plugboard = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}
        enigma = EnigmaMachine([rotor_I, rotor_II, rotor_III], reflector_B, plugboard)
        rotor_order_combinations = [
            [rotor_I, rotor_II, rotor_III],
            [rotor_I, rotor_III, rotor_II],
            [rotor_II, rotor_I, rotor_III],
            [rotor_II, rotor_III, rotor_I],
            [rotor_III, rotor_I, rotor_II],
            [rotor_III, rotor_II, rotor_I]
        ]
        if args.possible:
            possibilities = [p.upper() for p in args.possible]
            result = possibility_based_cracker(encoded_message, possibilities, enigma, rotor_order_combinations)
            if result:
                print(f"Decoded message: {result}")
            else:
                print("No match found with the given possibilities.")
        else:
            brute_force_cracker(encoded_message, enigma, rotor_order_combinations)
    if __name__ == "__main__":
        main()
except Exception as e:
    print(e)