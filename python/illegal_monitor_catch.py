import utils

import bblfsh

if __name__ == '__main__':
    client = bblfsh.BblfshClient("0.0.0.0:9432")

    uast = client.parse("../java/illegal_monitor_catch.java").uast
    catchs = bblfsh.filter(uast, "//CatchClause//SimpleType//Identifier[@Name='IllegalMonitorStateException']")

    for c in catchs:
        print("Don't catch IllegalMonitorStateException at line {}".format(c.start_position.line))