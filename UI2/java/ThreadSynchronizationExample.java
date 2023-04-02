import java.util.Arrays;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ThreadSynchronizationExample {
    public static void main(String[] args) throws InterruptedException {
        
        // Non-compliant stream usage with primitive types
        Arrays.asList(1, 2, 3, 4).stream() // Noncompliant
                .filter(i -> i > 2)
                .forEach(System.out::println);

        // Lock - wait
        final Lock lock = new ReentrantLock();
        final Condition notFull = lock.newCondition();

        lock.lock();
        try {
            notFull.await();
        } finally {
            lock.unlock();
        }

        // Thread.run, object wait
        Thread thread = new Thread(() -> {
            removeElement();
        });
        thread.start();
    }

    private static void removeElement() {
    while (!suitableCondition()) {
        wait();
		}
		//Perform removal
	}


    private static boolean suitableCondition() {
        // Check condition here
        return false;
    }
}
