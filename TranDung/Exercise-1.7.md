Exercise 1.7
7. Consider the following three example classes. These are OO faults taken from Joshua Bloch’s
Effective Java, Second Edition. Answer the following questions about each.
    
(a)
- The method clone() inside class Truck cannot use the clone() method of class Vehicle. One of possible modification is:

public class Vehicle implements Cloneable
{
    private int x;

    public Vehicle(int y) { x = y;}

    @Override public Object clone() {
        Object result = new Vehicle(this.x);
        return result;
    }
    @Override public boolean equals (Object o) {
        if (!(o instanceof Vehicle)) return false;
        Vehicle v = (Vehicle) o;
        return v.x == this.x;
    }
}
    
BigDecimalTest.java
The fault in is the inconsistency between methods compareTo() and equals(). One of possible modification is: Override one of them or overide methods in HashSet or TreeSet. 
    
Point.java, ColorPoint.java, PointTest.java 
The fault in is the inconsistency between superclass and subclass. One of possible modification is: Write same.
    
(b)
A test case that does not execute the fault in (Vehicle.java, Truck.java, CloneTest.java), does not call method Truck.equals().
    
No test case that can not execute the fault in (BigDecimalTest.java) or (Point.java, ColorPoint.java, PointTest.java).
    
(c)
A test case that executes the fault in (Vehicle.java, Truck.java, CloneTest.java) and does not create result in an error state, does not create an instance of a subclass.
    
A test case that executes the fault in (BigDecimalTest.java) and does not create result in an error state.
    
No test case that executes the fault in (Point.java, ColorPoint.java, PointTest.java) and does not create result in an error state.