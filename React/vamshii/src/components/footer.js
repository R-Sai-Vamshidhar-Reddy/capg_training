import React from 'react';

function Footer(){
    return(
        <footer style={styles.footer}>
            <p>&copy; {new Date().getFullYear()} My Website. All rights reserved.</p>
        </footer>
    );
}

const styles = {
    footer: {
        backgroundColor: '#333',
        color: 'white',
        padding: '10px',
        textAlign: 'center',
        position: 'fixed',
        bottom: 0,
        width: '100%'
    }
};

export default Footer;