class SwitchNoBreak {
    void test() {
        switch (myVariable) {
            case 1:
                foo();
                break;
            case 2:  // Both 'doSomething()' and 'doSomethingElse()' will be executed. Is it on purpose ?
                doSomething();
            default:
                doSomethingElse();
                break;
        }
    }
}
