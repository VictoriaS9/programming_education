
def get_max_value(data):
  data = ["one", "1", "two", "2", "ten", "10", "15", "-2", "some long text goes here", "16.9", "&"]
  l = list()
  for element in data:
    m = element.replace(" ", "")
    #print(m)
    if not m.isalpha() and not m=='&':
     #print(element)
     l.append(float(element))
  #print(l)
  #print(type(l))
  #print(max(l))
  return int(max(l))
data = ["one", "1", "two", "2", "ten", "10", "15", "-2", "some long text goes here", "16.9", "&"]
print(get_max_value(data))
