import sublime
import sublime_plugin


OPENING_BRACKETS = "{[("
CLOSING_BRACKETS = "}])"
BRACKETS = OPENING_BRACKETS + CLOSING_BRACKETS

def FindMatchingBracket(starting_bracket, starting_region, view, forward=True):
    if forward:
        bracket_to_find = CLOSING_BRACKETS[OPENING_BRACKETS.find(starting_bracket)]
        return view.find(bracket_to_find, starting_region.begin(), sublime.LITERAL)
    else:
        # This sucks because there's no find_reverse() method...
        bracket_to_find = OPENING_BRACKETS[CLOSING_BRACKETS.find(starting_bracket)]

        # Start from the last match and skip until we're behind the starting region again
        for region in reversed(view.find_all(bracket_to_find, sublime.LITERAL)):
            if region.begin() > starting_region.begin():
                continue
            return region


def TryAddMatchingBracket(char, region, view):
    # Find next closing bracket / prev opening bracket
    matching_bracket_region = FindMatchingBracket(char, region, view, forward=char in OPENING_BRACKETS)
    if not matching_bracket_region:
        return

    print("Found matching bracket", view.substr(matching_bracket_region), "at", matching_bracket_region.begin(), matching_bracket_region.end())

    # Clear selections
    view.sel().clear()

    # Make sure the original selection goes left-to-right
    normalized_region = sublime.Region(region.begin(), region.end())

    # Add original selection and the matching bracket
    view.sel().add(normalized_region)
    view.sel().add(matching_bracket_region)

class FindNextBracketUnderExpandCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # It doesn't make sense to do anything if there are multiple selections
        if len(self.view.sel()) > 1:
            print("No multi-selections!")
            return

        region = self.view.sel()[0]

        if region.size() > 1:
            print("Only one char selection please!")
            return

        if not region.empty():
            # Only one character selected, try to add its' matching bracket to selection
            char = self.view.substr(region)
            if char in BRACKETS:
                print("Found", char, "at", region.begin(), region.end())
                TryAddMatchingBracket(char, region, self.view)
        else:
            # No selection so see if we got a bracket on either side of the caret
            region_left_of_caret = sublime.Region(region.begin(), region.begin() + 1)
            char = self.view.substr(region_left_of_caret)
            if char in BRACKETS:
                print("Found", char, "at", region_left_of_caret.begin(), region_left_of_caret.end())
                TryAddMatchingBracket(char, region_left_of_caret, self.view)

            region_right_of_caret = sublime.Region(region.begin() - 1, region.begin())
            char = self.view.substr(region_right_of_caret)
            if char in BRACKETS:
                print("Found", char, "at", region_right_of_caret.begin(), region_right_of_caret.end())
                TryAddMatchingBracket(char, region_right_of_caret, self.view)
