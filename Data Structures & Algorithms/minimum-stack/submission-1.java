class MinStack {
    // ArrayList <Integer>
    ArrayList<Integer> stack;
    // min value
    int minValue = Integer.MAX_VALUE;
    ArrayList<Integer> pastMins;

    public MinStack() {
        // initialize the arraylist
        stack = new ArrayList<Integer>();
        pastMins = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        // .add
        stack.add(val);
        // someway to keep track if its a min or not
        if (minValue >= val){
            // replace the value
            minValue = val;
            // add to the stack of min past element
            pastMins.add(val);
        }
        // [-2,2]
    }
    
    public void pop() {
        // remove the element at length - 1 
        if (pastMins.get(pastMins.size()-1).equals(stack.get(stack.size() - 1))){
            // we are removing our min value !!!!!!!!!!
            pastMins.remove(pastMins.size()-1);
            if(pastMins.size()-1 >= 0){
                minValue = pastMins.get(pastMins.size()-1);
            }
            else{
                minValue = Integer.MAX_VALUE;
            }
        }
        stack.remove(stack.size() - 1);

        
    }

    private void reEvalMin(){

    }
    
    public int top() {
        // accesses element at lenght - 1
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        // returns the min value
        return minValue;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */