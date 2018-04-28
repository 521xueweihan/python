def scan(sentence):
        result = []
        words=sentence.split()
        length = len(words);
        while words:
            if words[0] in ['east','west','north','south']:
                result.append(('direction',words[0]))
            elif words[0] in ['go', 'kill', 'stop','eat']:
                result.append(('verb',words[0]))
            elif words[0] in ['door','bear','princess','cabinet']:
                result.append(('noun',words[0]))
            elif words[0] in['the','in','of','from','at','it']:
                result.append(('stop',words[0]))
            elif convert_number(words[0]):
                num = int(words[0])
                result.append(('number',num))
            else:
                result.append(('error',words[0]))
            words = words[1:]
        return result
        
def convert_number(s):
        try:
            return int(s)
        except ValueError:
            return None        
