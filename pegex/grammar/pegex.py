"""
Pegex Grammar module for pegex
"""

class Grammar():
    def __init__(self):
        self.tree = {}
        self.tree.update(
        { '+top': 'grammar',
  'all_group': { '.all': [ { '.ref': 'rule_item'},
                           { '+mod': '*',
                             '.all': [ { '.rgx': '\\s*'},
                                       { '.ref': 'rule_item'}]}]},
  'any_group': { '.all': [ { '.ref': 'rule_item'},
                           { '+mod': '+',
                             '.all': [ { '.rgx': '\\s*\\|\\s*'},
                                       { '.ref': 'rule_item'}]}]},
  'bracketed_group': { '.all': [ { '.rgx': '\\[\\s*'},
                                 { '.ref': 'rule_group'},
                                 { '.rgx': '\\s*\\]([\\*\\+\\?]?)'}]},
  'comment': { '.rgx': '(?:[\\ \\t]*\\r?\\n|\\#.*\\r?\\n)'},
  'error_message': { '.rgx': '`([^`\\r\\n]*)`'},
  'grammar': { '.all': [ { '+mod': '+',
                           '.all': [ { '+mod': '*', '.ref': 'comment'},
                                     { '.ref': 'rule_definition'}]},
                         { '+mod': '*', '.ref': 'comment'}]},
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
  'rule_reference': { '.rgx': '([!=]?)<([a-zA-Z]\\w*)>([\\*\\+\\?]?)'}}
        )

