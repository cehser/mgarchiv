import itertools

class Helpers:
  def to_ranges(iterable):
    iterable = sorted(set(iterable))
    for key, group in itertools.groupby(enumerate(iterable), lambda t: t[1] - t[0]):
      group = list(group)
      yield group[0][1], group[-1][1]

  def ranges_to_strs(ranges):
    return [str(a) if a==b  else str(a) + '-' +str(+b)  for a,b in ranges]
  
  def list_to_range_strs(list):
    return Helpers.ranges_to_strs(Helpers.to_ranges(list))