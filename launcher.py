from sys import exit
import speech_recognition as sr
import subprocess


def process_cmd(cmd):
  try:
    if cmd != "f***":
      subprocess.call(cmd)
    else:
      print("Don't you say that again! Fuck you!")
      exit(0)
  except OSError as e:
    print(e)


def initials(func):
  r = sr.Recognizer()
  m = sr.Microphone()

  def inner_wrapper():
    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("What you wanna launch? Say 'fuck' to exit")
            func(r, source)
    except KeyboardInterrupt:
        pass
  return inner_wrapper


@initials
def listen(r, source):
  while True:
    audio = r.listen(source)
    try:
        value = r.recognize(audio)
        if str is bytes:  # for Python 2
            print(u"You requested {} to run".format(value).encode("utf-8"))
        else:  # Python 3+
            print("You requested {} to run".format(value))
        print("Lemme check if the command is valid..")
        process_cmd(value.encode("utf-8").lower())
    except Exception as e:
        print(e)
        print("Oops! Didn't catch that. Mind trying again?")
    print("What you wanna launch next?")


def main():
  listen()

if __name__ == "__main__":
  main()
