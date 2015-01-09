import sublime, sublime_plugin
import re

class StringWrapperCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      # cursor_position = region.begin()
      line = self.view.line(region)
      line_contents = self.view.substr(line) + "\n"
      matches = re.search(r"""(?P<quote>['"]).*?(?P=quote)""", line_contents)
      if matches is None:
        rowcol = self.view.rowcol(region.begin())
        line_number = rowcol[0] + 1
        print("no match on line " + str(line_number))
        return
      print(matches)
      # self.view.insert(edit, line.begin(), line_contents) # duplicate line
      # self.view.insert(edit, cursor_position, "Current cursor position: " + str(cursor_position))
