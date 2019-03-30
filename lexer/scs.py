"""Pygments lexer for critic markup."""
from pygments.lexer import RegexLexer, include
from pygments import token

__all__ = ("SCsLexer",)


class SCsLexer(RegexLexer):

    name = 'SCs'
    aliases = ['scs', 'scsi']
    filenames = ['*.scs', '*.scsi']
    mimetypes = ['text/scs']

    keywords = [
        'sc_const', 'sc_var',
        # nodes
        'sc_node', 'sc_link', 'sc_edge_dcommon', 'sc_edge_ucommon', 'sc_edge_main', 'sc_edge_access',
        'sc_node_tuple', 'sc_node_struct', 'sc_node_role_relation', 'sc_node_norole_relation',
        'sc_node_class', 'sc_node_abstract', 'sc_node_material',
        # edges
        'sc_edge_pos', 'sc_edge_neg', 'sc_edge_fuz', 'sc_edge_perm', 'sc_edge_temp',
        # backward compatibility
        'sc_node_not_relation', 'sc_node_not_binary_tuple'
    ]

    def name_callback(lexer, match):
        text = match.group(0)
        if text in SCsLexer.keywords:
            yield match.start(), token.Keyword, text
        elif text.startswith('_'):
            yield match.start(), token.Name.Variable, text
        elif text.startswith('.'):
            yield match.start(), token.Name.Instance, text
        else:
            yield match.start(), token.Name.Constant, text

    tokens = {
        'connectors': [
            (r'\s*[_]?([-~][\/|]?)>\s*', token.Operator),
            (r'\s*[_]?<([\/|]?[-~])\s*', token.Operator),
            (r'\s*[_]?((=>)|(<=))\s*', token.Operator),
            (r'\s*([_]?<=>)|([.]{0,2}>|<[.]{0,2})\s*', token.Operator),
        ],
        'punctuation': [
            (r';;|;', token.Punctuation),
            (r'::|:', token.Punctuation),
            (r'\(\*|\*\)', token.Punctuation),
            (r'\[\*|\[', token.Punctuation),
            (r'\*\]|\]', token.Punctuation),
            (r'\{|\}', token.Punctuation),
            (r'=', token.Punctuation),
            ('#', token.Punctuation),
        ],
        'root': [
            (r'(\[\*)|(\*\])', token.String.Delimiter, 'root'),
            ('"', token.String.Other, 'url'),
            ('\[', token.String, 'content'),
            include('connectors'),
            include('punctuation'),
            (r'([_]?[.]{0,2})?([a-zA-Z0-9_]+)', name_callback),
            (r'/\*', token.Comment.Multiline, 'comment'),
            (r'//.*?$', token.Comment.Singleline),
            (r'\.\.\.', token.Name.Entity),
        ],
        'comment': [
            (r'[^*/]', token.Comment.Multiline),
            (r'/\*', token.Comment.Multiline, '#push'),
            (r'\*/', token.Comment.Multiline, '#pop'),
            (r'[*/]', token.Comment.Multiline)
        ],
        'content': [
            ('[^\]]+', token.String),
            (r'\\.', token.String.Escape),
            ('\]', token.String, '#pop'),
        ],
        'url': [
            ('[^"]+', token.String.Other),
            ('"', token.String.Other, '#pop'),
        ],
    }

    # def get_tokens_unprocessed(self, text):
    #     for index, token, value in RegexLexer.get_tokens_unprocessed(self, text):
    #         if token is token.Name and value in self.keywords:
    #             yield index, token.Keyword, value
    #         else:
    #             yield index, token, value