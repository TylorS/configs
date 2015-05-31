from snake import *

@when_buffer_is("python")
def setup_python(ctx):
    
    @key_map("<leader>r")
    def run():
        keys(",r")
