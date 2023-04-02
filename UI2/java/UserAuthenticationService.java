import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class UserAuthenticationService {
    public String authenticate(String username, String password) {
        MyUserDetailsService userDetailsService = new MyUserDetailsService();
        UserDetails userDetails = userDetailsService.loadUserByUsername(username);

        if (userDetails == null) {
            throw new BadCredentialsException(username + " doesn't exist in our database"); // Sensitive
        }

        // Perform authentication here using the UserDetails object

        return "Authentication successful";
    }

    public void configureAuthentication(AuthenticationManagerBuilder builder) {
        DaoAuthenticationProvider authenticationProvider = new DaoAuthenticationProvider();
        authenticationProvider.setUserDetailsService(new MyUserDetailsService());
        authenticationProvider.setPasswordEncoder(new BCryptPasswordEncoder());
        authenticationProvider.setHideUserNotFoundExceptions(false); // Sensitive
        builder.authenticationProvider(authenticationProvider);
    }
}
