# Custom reliable python calculator
import contextlib
import sys 

class BoldCalc():
    def __init__(self):
        self.vars = {}
    
    @staticmethod
    def is_assignment(cmd):
        c = cmd.count('=')
        if c > 1:
            raise Exception(f"invalid assignment '{cmd}'")
        if c == 1:
            return True
        return False

    def check_identifiers(self, a, b):
        try:
            a = a.strip()
            if not( a and a[0].isalpha() ):
                raise Exception
        except:
            raise Exception(f"invalid identifier '{a}'")
        try:
            b = b.strip()
            if b in self.vars.keys():
                b = self.vars[b]
            b = eval(b, self.vars)
            self.vars[a] = b
        except:
            raise Exception(f"invalid identifier '{b}'")

    @contextlib.contextmanager
    def run_command(self, cmd):
        cmd = cmd.strip()
        x = ''
        try:
            if cmd and not cmd[0] == '#':
                if self.is_assignment(cmd):
                    a, b = cmd.split('=')
                    self.check_identifiers(a, b)
                else:
                    x = eval(cmd, {}, self.vars)
        except Exception as e:
            x = e
        finally:
            yield x

    def start(self):
        cmd = sys.stdin.readline()
        while cmd:
            with self.run_command(cmd) as calc:
                if not calc is None:
                    print(calc)
            cmd = sys.stdin.readline()

calc = BoldCalc()
calc.start()