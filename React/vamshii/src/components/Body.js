import React from 'react';
import Greeting from '../greetings';
function Body(){
    return(
        <main style={styles.main}>
            <Greeting name="Vamshi"></Greeting>
            <h2>Welcome to my Website</h2>
            <p>This is a simple React application with a stuctured layout.</p>
        </main>
    );
}


const styles={
    main:{
        padding:'20px',
        textAlign:'center'
    }
}

export default Body;