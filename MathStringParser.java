import java.util.ArrayList;
import java.util.HashMap;

/*
* Ron Beavers
* 10/16/2017
Implement the following:

Write a function
Public double evalExpression(String expression) throws Exception;
This method should evaluate a simple math expression with numbers and operators, then return either a number that represents the value of the expression or an exception with a proper error message indicate why expression is not valid.

DO NOT USE THE SCRIPT ENGINE in JAVA

Valid numbers:
Any integer from -1000000 to 1000000

Valid operators : +, -, /, *
*/
public class MathStringParser {

    static final String ADD = "+";
    static final String SUB = "-";
    static final String DIV = "/";
    static final String MULTI = "*";
    static HashMap<String, Integer> operatorMap = new HashMap<>();


    //inner class for the stacks used
    static class MathStringParserStack {

        //Member variable
        private ArrayList<String> tokens;

        //Constructor
        public MathStringParserStack() {
            tokens = new ArrayList<String>();
        }

        //Stack accessor methods
        public boolean isEmpty() {
            return tokens.size() == 0;
        }

        public String top() {
            return tokens.get(tokens.size() - 1);
        }

        //Add and remove
        public void push(String t) {
            tokens.add(t);
        }

        public void pop() {
            tokens.remove(tokens.size() - 1);
        }
    }

    public static double evalExpression(String expression) throws Exception{

        MathStringParserStack operators = new MathStringParserStack();
        MathStringParserStack numbers = new MathStringParserStack();

        if(expression.length() == 0) {
            throw new Exception("Expression cannot be blank, otherwise there is nothing to calculate");
        }

        String [] split = expression.split("(?<=[-+*/])|(?=[-+*/])");

        for(String s : split){
            String stripped = s.trim();
            if(!isValidInteger(stripped) && !isValidOperator(stripped)){
                throw new Exception(stripped + "is not a valid argument. Calculations are only done with " +
                        "+,-,*,/ operators and valid integers in the range of -1000000 to 1000000.");
            }
            if(isValidInteger(stripped)){
                numbers.push(stripped);
            }
            if(isValidOperator(stripped)){
                System.out.println(operatorMap.get(stripped));
                if(operators.isEmpty() || operatorMap.get(operators.top()) < operatorMap.get(stripped)){
                    operators.push(stripped);
                }
                else {
                    while (!operators.isEmpty() && operatorMap.get(operators.top()) >= operatorMap.get(stripped)) {
                        rebalanceNumbersAndOperators(numbers, operators);
                    }
                    operators.push(stripped);
                }
            }
        }
        while(!operators.isEmpty()){
            String remainderB = numbers.top();
            numbers.pop();
            String remainderA = numbers.top();
            numbers.pop();
            String remainderOp = operators.top();
            operators.pop();
            numbers.push(String.valueOf(doMath(remainderA, remainderOp, remainderB)));
        }
        return Integer.parseInt(numbers.top());


    }

    public static void rebalanceNumbersAndOperators (MathStringParserStack numbers, MathStringParserStack operators){
        String b = numbers.top();
        numbers.pop();
        String a = numbers.top();
        numbers.pop();
        String operator = operators.top();
        operators.pop();
        numbers.push(String.valueOf(doMath(a, operator, b)));
    }

    public static boolean isValidInteger(String s) {
        try {
            Integer.parseInt(s);
        } catch(NumberFormatException e) {
            return false;
        }
        //check the valid integer range of -1000000 to 1000000
        if(Integer.parseInt(s) < -1000000 || Integer.parseInt(s) > 1000000){
            return false;
        }
        return true;
    }

    public static boolean isValidOperator(String s) {
        //on first check, we will fill the HashMap for the operators
        if(operatorMap.size() == 0){
            operatorMap.put("+", 1);
            operatorMap.put("-", 1);
            operatorMap.put("/", 2);
            operatorMap.put("*", 2);
        }

        return (operatorMap.containsKey(s));

    }

    public static int doMath(String a, String operator, String b){
        switch(operator){
            case ADD:
                return Integer.parseInt(a) + Integer.parseInt(b);
            case SUB:
                return Integer.parseInt(a) - Integer.parseInt(b);
            case DIV:
                return Integer.parseInt(a) / Integer.parseInt(b);
            case MULTI:
                return Integer.parseInt(a) * Integer.parseInt(b);
            default:
                return 0;
        }
    }

    public static void main(String [] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the mathematical expression that you'd like as a string. Only +, -, /, * operations allowed ");
        String expression = sc.next();
        System.out.println(evalExpression(expression));
    }

}
