import { Container } from '@mui/material';
import ResponsiveGrid from '../components/ResponsiveGrid';
import React from 'react';

interface Props {
    // Define your component props here
}

const Dashboard: React.FC<Props> = () => {
    // Add your component logic here

    return (
        <div>
            <Container maxWidth="lg">
                <h1>Your Notes</h1>
                <ResponsiveGrid />
            </Container>
        </div>
    );
};

export default Dashboard;