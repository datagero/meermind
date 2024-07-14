import { Container } from '@mui/material';
import ResponsiveGrid from '../components/ResponsiveGrid';
import React, { useEffect } from 'react';
import { Note } from "../types/Note"; // Update the path to the correct location of the 'Note' type file
import { NotesAPI }  from '../api/NotesAPI';
import { app } from '../api/configs/realmConfig';
import * as Realm from "realm-web";
interface Props {
    // Define your component props here
}

const Dashboard: React.FC<Props> = () => {
    // Add your component logic here

    const [notes, setNotes] = React.useState<Note[]>([])
    const [comments, setComments] = React.useState<any[]>([])
    useEffect(() => {
    NotesAPI.getAll().then((notes: any) => {
    const filteredNotes: Note[] = notes.data.map((note: any) => note.transcript_summary);
      setNotes(filteredNotes)
    })
  }, [])
    return (
        <div>
            <Container maxWidth="lg">
                <h1>Your Notes</h1>
                <ResponsiveGrid notes={notes || []} />
            </Container>
        </div>
    );
};

export default Dashboard;