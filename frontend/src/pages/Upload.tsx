import React, { useState, ChangeEvent, FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Button, Box, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { NotesAPI } from '../api/NotesAPI';
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
      NotesAPI.create(file).then((notes: any) => {
        setLoading(false);
        navigate('/')
      })
    }catch(e){
      console.log(e)
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 5 }}>
      <Typography variant="h4">Upload File</Typography>
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
    <h2>{file?.name}</h2>
    <Button type="submit" variant="contained" onClick={handleUpload}>
       Submit Transcript
      </Button>
      <h2>{loading&&'is Loading'}</h2>
    </Box>
  );
};

export default Upload;
