import sublime
import sublime_plugin


OPENING_BRACKETS = "{[("
CLOSING_BRACKETS = "}])"
BRACKETS = OPENING_BRACKETS + CLOSING_BRACKETS

class FindNextBracketUnderExpandCommand(sublime_plugin.TextCommand):
    def NextChar(self, point):
        return self.view.substr(point)

    def PrevChar(self, point):
        return self.view.substr(point - 1)

    def NextCharRegion(self, point):
        return sublime.Region(point, point + 1)

    def PrevCharRegion(self, point):
        return sublime.Region(point - 1, point)

    def matching_bracket(self, bracket):
        if bracket in OPENING_BRACKETS:
            return CLOSING_BRACKETS[OPENING_BRACKETS.find(bracket)]
        elif bracket in CLOSING_BRACKETS:
            return OPENING_BRACKETS[CLOSING_BRACKETS.find(bracket)]

    def MoveAndGetRegion(self, starting_region, mode):
        self.view.run_command("move_to", {"to": "brackets"})
        region_after_move = self.view.sel()[0]

        # Did we move forward?
        if starting_region.a < region_after_move.a:
            # Caret moves to the right side of the bracket so account for that
            if mode == "inside":
                return self.NextCharRegion(region_after_move.a)
            else:
                return self.PrevCharRegion(region_after_move.a)
        # Or backward?
        elif starting_region.a > region_after_move.a:
            # Caret moves to the left of the bracket
            if mode == "inside":
                return self.PrevCharRegion(region_after_move.a)
            else:
                return self.NextCharRegion(region_after_move.a)
        # No matching bracket found :(
        else:
            return None

    def ReplaceSelectionWith(self, selections):
        self.view.sel().clear()
        for selection in selections:
            self.view.sel().add(selection)

    def run(self, edit):
        # It doesn't make sense to do anything if there are multiple selections
        if len(self.view.sel()) > 1:
            return

        starting_region = self.view.sel()[0]

        # No selection allowed because running the command with no matching bracket
        # throws it away. Should save the original region and restore if needed.
        # There's also the issue of moving between brackets right next to each other
        # which needs to be detected.
        if starting_region.size() > 0:
            return

        # This is complicated. Moving within brackets moves the caret to the "inside"
        # of the next. If the caret is on the "outside" touching a brace, it moves
        # to the "outside". This means that moving between touching braces breaks,
        # i.e. with cursor in x:
        # (  x   ())
        # it selects the wrong braces.
        # Not sure how to fix.

        # If there's a bracket to the right of the caret, it'll move to its matching
        # caret's outside edge

        next_char = self.NextChar(starting_region.a)
        next_next_char = self.NextChar(starting_region.a + 1)
        prev_char = self.PrevChar(starting_region.a)

        # With | as the caret:
        # Handle "(|)"
        if prev_char in OPENING_BRACKETS and next_char in CLOSING_BRACKETS:
            region = sublime.Region(starting_region.a - 1, starting_region.a + 1)
            self.ReplaceSelectionWith([region])
        # Handle "|()(...)" etc
        elif next_char in OPENING_BRACKETS and next_next_char in CLOSING_BRACKETS:
            region = sublime.Region(starting_region.a, starting_region.a + 2)
            self.ReplaceSelectionWith([region])
        # Caret touching the outside edge
        elif next_char in OPENING_BRACKETS or prev_char in CLOSING_BRACKETS:
            mode = "outside"
        else:
            # This is the error prone situation described above
            mode = "inside"

        bracket1 = self.MoveAndGetRegion(starting_region=starting_region, mode=mode)
        if not bracket1:
            return
        bracket2 = self.MoveAndGetRegion(starting_region=bracket1, mode=mode)

        self.ReplaceSelectionWith([bracket1, bracket2])
