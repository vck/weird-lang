TEST_FILE = "test.han"

def parse(token):
   with open("GRAMMAR") as grammar:
      for gram in grammar:
         print(f"checking for {gram}")
         if gram.strip("\n").split()[1] == token:
            return gram
      else:
         return None

def run(test_file):
   with open(TEST_FILE) as TOKENS:
      for token in TOKENS:
         print(token.strip("\n"), parse(token.strip("\n")))

if __name__ == "__main__":
   run("test.han")
