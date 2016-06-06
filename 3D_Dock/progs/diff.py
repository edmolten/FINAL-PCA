def get_data_from_file(file_name):
  output_file = open(file_name,"r")
  data = []
  data_lines = []
  for line in output_file:
    if line.strip() == "Starting main loop through the rotations":
      for data_line in output_file:
        if data_line.strip() == "PCA TIMING SHOULD stop here":
          break
        data_lines.append(data_line.split())
  for i in range(0,len(data_lines),3):
    line1 = data_lines[i]
    line2 = data_lines[i+1]
    line3 = data_lines[i+2]
    coords1 = (line1[4],line1[5],line1[6])
    coords2 = (line2[4],line2[5],line2[6])
    coords3 = (line3[4],line3[5],line3[6])
    score1 = int(line1[3])
    score2 = int(line2[3])
    score3 = int(line3[3])
    scores = []
    scores.append(score1)
    scores.append(score2)
    scores.append(score3)
    coords = set()
    coords.add(coords1)
    coords.add(coords2)
    coords.add(coords3)
    data.append((scores,coords))
  output_file.close();
  return data

def compare(data_list1,data_list2):
  lenght = len(data_list1)
  for i in range(lenght):
    data1 = data_list1[i]
    data2 = data_list2[i]
    scores1 = data1[0]
    coords1 = data1[1]
    scores2 = data2[0]
    coords2 = data2[1]
    good_scores = 0
    for score1 in scores1:
      for score2 in scores2:
        if score2 - 2 <= score1 <= score2 + 2:
          good_scores += 1
      if good_scores < 1:
        return False
      else:
        good_scores = 0
    if coords1 != coords2:
      return False
  return True

data_list1 = get_data_from_file("out1")
data_list2 = get_data_from_file("out2")
print compare(data_list1,data_list2)
