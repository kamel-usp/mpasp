from IPython.core.magic import Magics, magics_class, line_cell_magic, output_can_be_silenced
from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

@magics_class
class PaspMagic(Magics):
  @magic_arguments()
  @argument("-p", "--program", default=False, action="store_true", \
            help="Return program instead of output of program.")
  @argument("-q", "--quiet", default=False, action="store_true", \
            help="Run in quiet mode.")
  @argument("code", type=str, nargs='?', default=None, \
            help="Additional code (as string) to be parsed as dPASP program. Surround with single " \
            "quotation marks if passing as a variable (e.g. '{my_var}').")
  @line_cell_magic
  def pasp(self, line, cell=None):
    "Line and cell magic for dPASP."
    args = parse_argstring(self.pasp, line)
    if cell is None:
      # Line magic.
      raise NotImplementedError("Line magic for dPASP is not yet supported.")
    else:
      # Cell magic.
      import pasp, wurlitzer
      P = pasp.parse(f"{args.code[1:-1]}\n{cell}" if args.code is not None else cell, from_str=True)
      with wurlitzer.sys_pipes():
        r = P if args.program else P(quiet=args.quiet)
      return r
