class MyStack {
    ArrayDeque<Integer> queue1;
    ArrayDeque<Integer> queue2;

    public MyStack() {
        queue1 = new ArrayDeque<Integer>();
        queue2 = new ArrayDeque<Integer>();
    }
    // queue.addLast(element);
    // queue.removeFirst(); returns val
    public void push(int x) {
        queue2.addLast(x);

        while(!queue1.isEmpty()){
            int element = queue1.removeFirst();
            queue2.addLast(element);
        }

        // add back to queue1
        while(!queue2.isEmpty()){
            int element = queue2.removeFirst();
            queue1.addLast(element);
        }
    }
    
    public int pop() {
        return queue1.removeFirst();
    }
    
    public int top() {
        return queue1.peek();
    }
    
    public boolean empty() {
        return queue1.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */