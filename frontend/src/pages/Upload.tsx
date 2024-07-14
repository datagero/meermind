import React, { useState, ChangeEvent, FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Button, Box, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { NotesAPI } from '../api/NotesAPI';
import Paper from '@mui/material/Paper';
const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

const Upload: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading,setLoading] = useState<Boolean>(false);
  const navigate = useNavigate();

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
      console.log(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      return;
    }
    setLoading(true);
    try{
      NotesAPI.create(file).then((response) => {
        console.log("HASH ID",response);
        setLoading(false);
        navigate(`/note/${response}`);
      })
    }catch(e){
      console.log(e)
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 5 , p: 3}}>
      <Paper elevation={3} sx={{ p: 3 , alignItems: 'center', justifyContent: 'center'}}>
      <Typography variant="h4">Upload Your Transcript</Typography>
      <br />
      <Button
      component="label"
      role={undefined}
      variant="contained"
      tabIndex={-1}
      startIcon={<CloudUploadIcon />}
    >
      Upload file
      <VisuallyHiddenInput type="file" onChange={handleFileChange}/>
    </Button>
    <br />
   { file && <Typography variant="body1" sx={{ mt: 2 }}>uploaded file: {file?.name}</Typography>}
   <br />
    <Button type="submit" variant="contained" onClick={handleUpload}>
       Submit Transcript
      </Button>
      <h2>{loading&&'is Loading'}</h2>
      </Paper>
    </Box>
  );
};

export default Upload;
