"""
Pegex Grammar module for pegex
"""

class Grammar():
    def __init__(self):
        self.tree = {}
        self.tree.update(
        { '+top': 'grammar',
  'all_group': { '.ref': 'rule_part', '.sep': { '.rgx': '\\s*'}},
  'any_group': { '.all': [ { '.ref': 'rule_part'},
                           { '+qty': '+',
                             '.all': [ { '.rgx': '\\s*\\|\\s*'},
                                       { '.ref': 'rule_part'}]}]},
  'bracketed_group': { '.all': [ { '.rgx': '(\\.?)\\[\\s*'},
                                 { '.ref': 'rule_group'},
                                 { '.rgx': '\\s*\\]([\\*\\+\\?]?)'}]},
  'comment': { '.rgx': '(?:[\\ \\t]*\\r?\\n|\\#.*\\r?\\n)'},
  'error_message': { '.rgx': '`([^`\\r\\n]*)`'},
  'grammar': { '.all': [ { '+qty': '+',
                           '.all': [ { '+qty': '*',
                                       '-skip': 1,
                                       '.ref': 'comment'},
                                     { '.ref': 'rule_definition'}]},
                         { '+qty': '*', '-skip': 1, '.ref': 'comment'}]},
  'regular_expression': { '.rgx': '/([^/\\r\\n]*)/'},
  'rule_definition': { '.all': [ { '.rgx': '\\s*'},
                                 { '.ref': 'rule_name'},
                                 { '.rgx': '[\\ \\t]*:\\s*'},
                                 { '.ref': 'rule_group'},
                                 { '.ref': 'rule_ending'}]},
  'rule_ending': { '.rgx': '\\s*?(?:\\n\\s*|;\\s*|\\z)'},
  'rule_group': { '.any': [{ '.ref': 'any_group'}, { '.ref': 'all_group'}]},
  'rule_item': { '.any': [ { '.ref': 'rule_reference'},
                           { '.ref': 'regular_expression'},
                           { '.ref': 'bracketed_group'},
                           { '.ref': 'error_message'}]},
  'rule_name': { '.rgx': '([a-zA-Z]\\w*)'},
  'rule_part': { '.all': [ { '.ref': 'rule_item'},
                           { '+qty': '?',
                             '.all': [ { '.rgx': '\\s*\\s\\*\\*\\s\\s*'},
                                       { '.ref': 'rule_item'}]}]},
  'rule_reference': { '.rgx': '([!=\\+\\-\\.]?)<([a-zA-Z]\\w*)>([\\*\\+\\?]?)'}}
        )

