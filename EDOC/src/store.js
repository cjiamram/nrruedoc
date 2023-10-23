class AuthService {
    static getUserId() {
      return localStorage.getItem('userId');
    }
  
    static setUserId(userId) {
      localStorage.setItem('userId', userId);
    }
  
    static removeUserId() {
      localStorage.removeItem('userId');
    }
  }
  
  export default AuthService;