import { Container } from '@mui/material';
import ResponsiveGrid from '../components/ResponsiveGrid';
import React, { useEffect } from 'react';
import { Note } from "../types/Note"; // Update the path to the correct location of the 'Note' type file
import { NotesAPI }  from '../api/NotesAPI';
interface Props {
    // Define your component props here
}

const Dashboard: React.FC<Props> = () => {
    // Add your component logic here
    const [notes, setNotes] = React.useState<Note[]>([])

    useEffect(() => {
    NotesAPI.getAll().then((notes: any) => {
      // response handling
      setNotes(notes)
      console.log("NOTES", notes)
    })
  }, [])
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